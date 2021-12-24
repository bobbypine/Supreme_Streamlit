import Keyword
import streamlit as st
from urllib.error import URLError
import time


st.image('Supreme_Logo.png')
mobile_mode = st.checkbox('Mobile Mode')

try:
    userkey = st.text_input(label='Enter Your Keyword').strip()

except URLError as e:
    st.error(f'This Demo Requires Internet Access: {e.reason}')


def run():
    if userkey == "":
        st.write('Keyword Cannot Be Blank')
        st.stop()
    else:
        keyword = userkey.lower()
        keylist = keyword.split(",")

    for keyword in keylist:
        Keyword.keysearch(keyword, mobile=mobile_mode)

    for _ in range(600):
        try:
            if not Keyword.mylists:
                st.write('{}: Product Not Found for {}, Will Look Again...'.format(time.strftime("%I:%M:%S"),keyword).title())
                time.sleep(0.25)
                Keyword.keysearch(keyword, mobile=mobile_mode)
        except Exception as e:
            st.write('{}: or Webstore Closed'.format(e))
    st.write('Program Ended')
    st.write('------------------------------------------------------------------------------------------------------------')


if __name__ == "__main__":
    run()

    with st.expander("Feel Like Donating?"):
        st.write("This app is free, but donations are appreciated.")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('paypal.png', use_column_width=True)

        with col2:
            st.image('cashapp.png', use_column_width=True)

        with col3:
            st.image('venmo.jpg', use_column_width=True)