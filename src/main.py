import streamlit as st
import requests
import asyncio
import json
from PIL import Image

async def detect(image_file):
    URL = "https://yompdetectcode.azurewebsites.net/api/Detect_Products?code=w63hPwyKghVDMi40tHVEZhUujysngUlvSkUb1Mr7dGyMySFaVn6P0g=="
    image_data = image_file.read()
    headers = {'Content-Type': 'image/jpeg',"token":"7aea53bd41045422b5812a758a9d00d5"}
    response = requests.post(URL, headers=headers, data=image_data)
    return response.json()
    
    
clicked = False

async def main():
    st.set_page_config(page_title="Object Detecition API", page_icon="🤖", layout="wide")
    logo =Image.open("logo_stk.png")
    st.image(logo)
    st.title("Object Detecition API")
    st.header("Image Upload")
    image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    
    
    column1, column2 = st.columns(2)

    
    with column1:
        
        if image is not None:
            st.markdown("## Image Preview")
            st.write("---")
            st.image(image, use_column_width=True)
            
    clicked = st.button("Detect Objects")
    if clicked:
        with column2:
            st.empty()
            res = await detect(image)
            st.markdown("## Detected Objects")
            st.write("---")
            im = Image.open(requests.get(res.get("url"), stream=True).raw)
            st.image(im, use_column_width=True)
        st.markdown("## JSON Response")
        res_str = json.dumps(res, indent=4)
        st.code(res_str, language="json")
            
        
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())