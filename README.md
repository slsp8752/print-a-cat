# The Print-a-Cat Button
### Augment your printer to print cats using the Amazon Dash button

#### Installation
##### Dash Button Setup
* Follow the instructions [here](https://www.amazon.com/gp/help/customer/display.html?nodeId=201746340) for setting up your Dash button, but **only do steps 1 through 5.** ***Do not do step 6!***

* Optional: Go to your phone's settings and disable amazon notifications. Your phone will tell you to finish setting up your dash button every time you press it unless you do this step. On Android, this is done by going to 
```
Settings -> Applications -> Application manager -> Amazon -> Notifications -> Turn off 'Allow Notifications'
```

##### Script Installation
* Install python and pip, if they aren't already installed

* Run the following command in the main directory to install the required python packages

```
pip install -r requirements.txt
```
* Optional: If you want access to a bigger pool of cat images, you can add an api key to catPrintServer.py
You can apply for an API key [here](http://thecatapi.com/api-key-registration.html)
Then, add your key to the end of line 9 like so
```
api_key = "YOUR_API_KEY_HERE"

```

#### Usage

Note: The following commands have to be run with sudo in order to be able to listen for the button press

* First, you'll need to get the MAC address of your Dash button by running the following command in the main directory
```
sudo ./getMac.py
```
* Copy that MAC address and replace the MAC address on line 20 of catPrintServer.py

* To start listening for the Amazon Dash button, run the following command in the main directory
```
sudo ./catPrintServer.py
```

Now press your button! After a little bit of a wait, you should have a cat come out of your default printer!

