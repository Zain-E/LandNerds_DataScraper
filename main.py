# This is a sample Python script.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError
from google.oauth2.service_account import Credentials
from datetime import datetime
cookies = {
    'zooplapsid': 'a6b5134902dfd23940704ce0dc35f6ca',
    '_ga': 'GA1.3.1483749591.1652981863',
    'ajs_anonymous_id': '90988938-5dc1-432c-9633-8f1e03b3f590',
    'zooplasid': '4a58d17ef0a87c95418947cd35370bb5',
    '_gid': 'GA1.3.731505751.1654036191',
    'cookie_consents': '{"schemaVersion":4,"content":{"brand":1,"consents":[{"apiVersion":1,"stored":false,"date":"Tue, 31 May 2022 22:30:07 GMT","categories":[{"id":1,"consentGiven":true},{"id":3,"consentGiven":false},{"id":4,"consentGiven":false}]}]}}',
}

headers = {
    'authority': 'api-graphql-lambda.prod.zoopla.co.uk',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8,de;q=0.7',
    'origin': 'https://www.zoopla.co.uk',
    'referer': 'https://www.zoopla.co.uk/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'x-api-key': '3Vzj2wUfaP3euLsV4NV9h3UAVUR3BoWd5clv9Dvu',
}
dt = datetime.today().strftime('%Y%m%d')
ptypes = ['Detached','Semi-detached','Terraced','Terrace','Flat','Bungalow','Farm/land','Park home']
dict2 = {}
page_num = 0
while True:

    json_data = {
        'operationName': 'getListingData',
        'variables': {
            'path': f'/for-sale/property/england/?added=24_hours&pn={page_num}',
        },
        'query': 'query getListingData($path: String!) {\n  breadcrumbs(path: $path) {\n    label\n    tracking\n    uri\n    noAppend\n    i18nLabelKey\n    __typename\n  }\n  seoAccordions(path: $path) {\n    category\n    expanded\n    geo\n    name\n    propertyType\n    section\n    transactionType\n    rows {\n      links {\n        category\n        geo\n        propertyType\n        section\n        transactionType\n        uri\n        __typename\n      }\n      __typename\n    }\n    links {\n      category\n      geo\n      propertyType\n      section\n      transactionType\n      uri\n      __typename\n    }\n    __typename\n  }\n  discoverMore(path: $path) {\n    housePricesUri\n    findAgentsUri\n    __typename\n  }\n  searchResults(path: $path) {\n    analyticsTaxonomy {\n      url\n      areaName\n      activity\n      brand\n      countryCode\n      countyAreaName\n      currencyCode\n      listingsCategory\n      outcode\n      outcodes\n      page\n      postalArea\n      radius\n      radiusAutoexpansion\n      regionName\n      resultsSort\n      searchGuid\n      searchIdentifier\n      section\n      searchLocation\n      viewType\n      searchResultsCount\n      expandedResultsCount\n      totalResults\n      emailAllFormShown\n      emailAllTotalAgents\n      bedsMax\n      bedsMin\n      priceMax\n      priceMin\n      location\n      propertyType\n      __typename\n    }\n    analyticsEcommerce {\n      currencyCode\n      impressions {\n        id\n        list\n        position\n        variant\n        __typename\n      }\n      __typename\n    }\n    adTargeting {\n      activity\n      areaName\n      bedsMax\n      bedsMin\n      brand\n      brandPrimary\n      countyAreaName\n      countryCode\n      currencyCode\n      listingsCategory\n      outcode\n      outcodes\n      page\n      postalArea\n      priceMax\n      priceMin\n      propertyType\n      regionName\n      resultsSort\n      searchLocation\n      searchResultsCount\n      section\n      totalResults\n      url\n      viewType\n      __typename\n    }\n    metaInfo {\n      title\n      description\n      canonicalUri\n      __typename\n    }\n    pagination {\n      pageNumber\n      totalResults\n      totalResultsWasLimited\n      __typename\n    }\n    listings {\n      regular {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          branchId\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      extended {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          branchId\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      featured {\n        numberOfVideos\n        numberOfImages\n        numberOfFloorPlans\n        numberOfViews\n        listingId\n        title\n        publishedOnLabel\n        publishedOn\n        availableFrom\n        priceDrop {\n          lastPriceChangeDate\n          percentageChangeLabel\n          __typename\n        }\n        isPremium\n        featuredType\n        highlights {\n          description\n          label\n          url\n          __typename\n        }\n        otherPropertyImages {\n          small\n          large\n          caption\n          __typename\n        }\n        branch {\n          name\n          branchDetailsUri\n          phone\n          logoUrl\n          __typename\n        }\n        features {\n          content\n          iconId\n          __typename\n        }\n        image {\n          src\n          caption\n          responsiveImgList {\n            width\n            src\n            __typename\n          }\n          __typename\n        }\n        transports {\n          title\n          poiType\n          distanceInMiles\n          features {\n            zone\n            tubeLines\n            __typename\n          }\n          __typename\n        }\n        flag\n        listingId\n        priceTitle\n        price\n        alternativeRentFrequencyLabel\n        address\n        tags {\n          content\n          __typename\n        }\n        listingUris {\n          contact\n          detail\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    filters {\n      fields {\n        group\n        fieldName\n        label\n        isRequired\n        inputType\n        placeholder\n        allowMultiple\n        options\n        value\n        __typename\n      }\n      __typename\n    }\n    links {\n      saveSearch\n      createAlert\n      __typename\n    }\n    sortOrder {\n      currentSortOrder\n      options {\n        i18NLabelKey\n        value\n        __typename\n      }\n      __typename\n    }\n    seoBlurb {\n      category\n      transactionType\n      __typename\n    }\n    title\n    userAlertId\n    savedSearchAndAlerts {\n      uri\n      currentFrequency {\n        i18NLabelKey\n        value\n        __typename\n      }\n      __typename\n    }\n    polyenc\n    __typename\n  }\n}\n',
    }
    response = requests.post('https://api-graphql-lambda.prod.zoopla.co.uk/graphql', cookies=cookies, headers=headers, json=json_data)
    if page_num == 0:
        print('Estimated time of completion: ', int(response.json()['data']['searchResults']['pagination']['totalResults'] / 25 * 23 / 60),'minutes.')

    print('\nScraping page #',page_num+1)
    listings = response.json()['data']['searchResults']['listings']['regular']
    if len(listings) == 0:
        print('Completed.')
        break
    for listing in listings:
        d = listing
        dict1={}
        id1 = d['listingId']
        dict1['url'] = 'https://www.zoopla.co.uk'+d['listingUris']['detail']
        address = d['address']
        f = d['features']
        for i in f:
            dict1[i['iconId']] = i['content']
#         property_type = ''
#         for pt in ptypes:
#             if pt.lower() in d['title'].lower():
#                 property_type = pt
#         if property_type == '':
#             try:
#                 property_type = d['title'].split('bed ')[1].split(' ')[0]
#             except:
#                 property_type = ''
        params = {
            'search_identifier': 'd5b91e20173efcc3a6d06c92ef1a9fd2',
        }
        ln = dict1['url']
        while True:
            try:
                response = requests.get(f'https://translate.google.com/translate?anno=2&depth=1&pto=aue,ajax,boq&rurl=translate.google.com&sp=nmt4&u={ln}',headers=headers,timeout=30)
                lat = response.text.split('"latitude": ')[1].split(',')[0]
                break
            except:
                time.sleep(60)
                continue
        try:
            postcode = response.text.split('"postalCode": "')[1].split('"')[0]
            postcode_district = postcode.split(' ')[1]
            outcode = postcode.split(' ')[0]
        except:
            postcode = ''
            postcode_district = ''
            outcode = ''
        try:
            lat = response.text.split('"latitude": ')[1].split(',')[0]
            lon = response.text.split('"longitude": ')[1].split('\n')[0].strip()
        except:
            time.sleep(90)
            print('Retrying ... ')
            continue
        property_type =response.text.split('"propertyType":"')[1].split('"')[0]
        dict1['property_type'] = property_type
        dict1['postcode'] = postcode
        dict1['outcode'] = outcode
        dict1['postcode_district'] = postcode_district
        dict1['display_address'] = address.replace(postcode,outcode)
        dict1['price'] = d['price']
        dict1['latitude'] = lat
        dict1['longitude'] = lon
        dict2[id1] = pd.DataFrame(dict1,index=[0])
        sys.stdout.write(".")
        sys.stdout.flush()
    page_num += 1

df = pd.concat(dict2.values(),sort=False)
df['listing_condition']='pre-owned'

df['price'] = pd.to_numeric(df["price"].replace("[£,]", "", regex=True), errors ='coerce').fillna(0).astype('int')
df = df.rename(columns={'chair': 'num_recepts','bed':'num_beds','bath':'num_baths'})

df = df[['property_type','price','postcode_district','num_baths','postcode','outcode',
    'display_address','num_recepts','num_beds','url','listing_condition','latitude','longitude']]

df.to_excel(f'{dt}.xlsx',index=False)

target_table = f"propertysourcer_dailyhouseprices.{dt}"
project_id = "landnerds"
credential_file = "landnerds-31cdd6b25363.json"
credential = Credentials.from_service_account_file(credential_file)
job_location = 'US'

df.to_gbq(target_table, project_id=project_id, if_exists='replace',
          location=job_location, progress_bar=True, credentials=credential)
print(f'{dt} - Data saved in Bigquery.')