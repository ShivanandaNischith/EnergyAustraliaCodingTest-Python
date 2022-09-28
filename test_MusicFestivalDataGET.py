import requests

# API URl
url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"

def test_Should_return_200_Success_Code():
    response = requests.get(url)
    assert response.status_code == 200

def test_Should_return_MusicFestival_Band_Names():
    response = requests.get(url)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    if response_body != None:
        print('Test is returning MusicFestival Band Names')
    else:
        print('Test failed, as no data available')

def test_Checking_for_Throttled_Or_Status_Code_429():
    response = requests.get(url)
    counter = 1
    while response.status_code != 429:
        response = requests.get(url)
        counter = counter + 1
    assert response.status_code == 429
    print("The number of calls made to get Throttled / StatusCode429 =", counter)

