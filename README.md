# NASA Space Data Pipeline

## What this project does
Fetches real time astronomy data from NASA API 
and stores it automatically in AWS S3 bucket.

## Tools Used
- Python 3
- NASA APOD API
- AWS EC2 (Amazon Linux)
- AWS S3
- AWS IAM Role
- Git and GitHub

## Project Architecture
NASA API → Python Script → AWS S3

## Steps to Run
1. Launch EC2 instance on AWS
2. Install Python and boto3
3. Set NASA API key as environment variable
4. Run nasa_fetch.py
5. Data gets saved to S3 bucket automatically

## Skills Demonstrated
- Cloud infrastructure setup on AWS
- Python scripting for API integration
- Secure credential management
- AWS S3 storage integration
- Git version control
