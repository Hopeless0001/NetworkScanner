<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a simple network scanner I made in python utilizing nmap to scan for ip addresses.

It usually takes around 20 seconds to fully scan your network, and then displays the results in a neat little table.
 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

* python
  >sudo apt install python3.10
* pip
  >sudo apt install python3-pip

### Installation

1. Clone the repo
   >git clone https://github.com/Hopeless0001/NetworkScanner
2. Cd into the folder
   >cd NetworkScanner
3. Install pip packages
   >pip3 install -r requirements.txt


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Cd into the folder
   >cd NetworkScanner
2. Run main.py
   >python main.py

Now just press enter to scan 192.168.1.1-255.
Or optionally type in a custom starting ip such as 10.0.10.1

It will now scan the network for ip addresses and display their mac address, ip and host name. Usually takes around 20 seconds to scan.

If you do not like the colors you can change them in colors.py



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add Port Scanner
- [ ] Create An Optional GUI


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

