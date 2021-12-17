import Keyword
import streamlit as st
from urllib.error import URLError
import time
import sys

st.image('Supreme_Logo.png')

try:

    userkey = st.text_input(label='Enter Your Keyword')

except URLError as e:
    st.error(f'This Demo Requires Internet Access: {e.reason}')


if __name__ == "__main__":
    if userkey == "":
        st.write('Keyword Cannot Be Blank')
        # sys.exit()
        st.stop()
    else:
        keyword = userkey.lower()
        keylist = keyword.split(",")

    for keyword in keylist:
        Keyword.keysearch(keyword)

    for _ in range(600):
        try:
            if not Keyword.mylists:
                st.write('{}: Product Not Found for {}, Will Look Again...'.format(time.strftime("%I:%M:%S"),keyword).title())
                time.sleep(0.25)
                Keyword.keysearch(keyword)
        except Exception as e:
            st.write('{}: or Webstore Closed'.format(e))
    st.write('Program Ended')
    st.write('------------------------------------------------------------------------------------------------------------')
