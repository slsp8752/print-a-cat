# The Print-a-Cat Button
### Augment your printer to print cats using the Amazon Dash button
**Note:** Currently tested on Linux and OSX. Windows testing coming soon.
![Cat Print Button](http://i.imgur.com/72GDvqv.jpg)
#### Installation
**Note:** You need an Amazon Dah Button to use this! Unfortunately, they are only available to Amazon Prime members. If you are a student with an active .edu email address, you can sign up for a free trial of Amazon Prime. If you aren't I'm sure you can find someone that has Amazon Prime. You can purchase them [here](http://www.amazon.com/b?node=10667898011). It doesn't matter which button you choose.

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
If that doesn't work, you can try 
```
python -m pip install -r requirements.txt
```

* Optional: If you want access to a bigger pool of cat images, you can add an API key to catPrintServer.py
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

