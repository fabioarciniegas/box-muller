from time import sleep
from urllib import request
import os
import sys
from random import gauss
import argparse


def cli():
    parser = argparse.ArgumentParser(
        description='Generate random numbers according to normal distribution'
    )
    parser.add_argument("mu", type=float, help="mean of the normal distribution")
    parser.add_argument("sigma", type=float, help="standard deviation of the normal distribution")
    parser.add_argument("number_of_samples", type=int, help="number of samples to generate")
    args = parser.parse_args()
    try:
        generate_numbers(args.mu, args.sigma, args.number_of_samples)
    except Exception as e:
        print(e)
        sys.exit(os.EX_CONFIG)


def generate_numbers(mu, sigma, n):
    for i in range(n):
        sleep(abs(gauss(mu, sigma)))
        try:
            r = request.urlopen("http://helloworld-alb-1833288600.us-west-2.elb.amazonaws.com/")
            #print(r.read().decode('utf-8'))
            if i % 10 == 0:
                print("Generated {} requests".format(i))
        except Exception as e:
            print(e.read().decode('utf-8'))

if __name__ == "__main__":
    cli()
