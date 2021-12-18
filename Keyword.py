import webbrowser
import json
import requests
import time
import logging
import streamlit as st
import streamlit.components.v1 as components


def link_maker(url):
    html = '''
        <!DOCTYPE html>
        <html>


        <script>
        function myFunction() {
          window.open(#);
        }

        myFunction()

        </script>

        </body>
        </html>'''.replace('#', url)
    return html
    print(html)


def keysearch(keyword):

    logging.basicConfig(level=logging.INFO, filename='Supreme_Log.log', filemode='a',
                        format = " %(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %I:%M:%S %p ")
    starttime = time.time()
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    response = requests.get(url=url)
    data = json.loads(response.content.decode('utf-8'))
    mylist = []
    global mylists
    mylists = mylist
    for items in data['products_and_categories']:
        if items != 'new':
            categories = items
        for x in categories.split():
            for result in data['products_and_categories']['{}'.format(x)]:
                if keyword in result['name'].lower():
                    st.write('Product Found!')
                    name = result['name']
                    id = result['id']
                    if str(id)[0] == '3':
                        region = 'Supreme EU'
                    else:
                        region = 'Supreme US'
                    cat = result['category_name']
                    price = '${}'.format(result['price']*.01)
                    link = 'https://www.supremenewyork.com/shop/{}/{}'.format(x, id)
                    mylist.append(id)
                    st.write(name,'-',cat, '-', price)
                    st.write('\n')
                    st.write('Product Found at {} and Opened in {:.2f} Seconds'.format(time.strftime("%I:%M:%S"),time.time()-starttime))
                    html_data = link_maker(link)
                    components.html(html_data)
                    logging.info('{}: {} Found Using "{}" at {} and Opened in {:.2f} Seconds'.format(region, name, keyword, time.strftime("%I:%M:%S"),time.time()-starttime))





