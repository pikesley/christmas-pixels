# Christmas Pixels

I got [some of these NeoPixels](https://www.ebay.co.uk/itm/5V-50pcs-WS2811-Diffused-Digital-RGB-LED-Pixel-String-Module-Lights-Waterproof/372795105807) and thought it might be nice to make them into Christmas lights using a[Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/), so here we are

## On the Pi

### Hardware setup

I have the data line for the NeoPixels connected to [logical pin 18 (physical 12)](https://pinout.xyz/) on the Pi, but note that I had to connect this to the other end of the light string from where I connected the power, so I've effectively made a loop. I couldn't get anything to work with the data at the same end, or with the power at the other end. Possibly I'm doing something boneheaded, but it's no big deal.

Of more interest is the fact that these LEDs are GRB, not RGB. Once again, no big deal, but I'm led to understand that it's the luck of the draw which type you end up with.

### Software

I started with a bare-bones [NOOBS 3.2](https://www.raspberrypi.org/downloads/noobs/) install of [Raspbian Lite](https://www.raspberrypi.org/downloads/raspbian/), then:

#### Make Python 3 the default

```
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
```

(I heard this can cause havoc with `apt`, but it seems to be OK)

#### Install PIP

```
sudo apt-get update
sudo apt install -y python3-pip
```

## On your local machine

```
git clone https://github.com/pikesley/christmas-pixels
cd christmas-pixels
make build
make run
```

### Then on the container

```
make  # to run the tests
make push-code  # to push the code to the Pi
```

Note that the second step here assumes your Pi is named `xmas`, you might need to sweeten to taste

## Back on the Pi

```
make systemd-install
```

And then you should probably reboot. Lights should start blinking when it comes back up, and it should be logging to `/var/log/lightsserver.*`
