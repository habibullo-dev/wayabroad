# import os
# import boto3
# from dotenv import load_dotenv, find_dotenv
# from pymongo import MongoClient

# load_dotenv(find_dotenv())

# password = os.environ.get("MONGODB_PWD")
# connection = f"mongodb+srv://toby:{password}@wayabroad.ytg2mkg.mongodb.net/?retryWrites=true&w=majority&appName=wayabroad"

# client = MongoClient(connection)

# db = client['yourDatabaseName']  # replace 'yourDatabaseName' with the name of your database
# universities_collection = db['universities']  # creates a new collection named 'universities'

# # Insert a document into the 'universities' collection
# university_document = {
#     "name": "Test University",
#     "location": "Test Location",
#     "brief_info": "This is a test university.",
#     "image_url": "http://example.com/test.jpg",
#     "application_period": "2022-01-01 to 2022-12-31"
# }

# universities_collection.insert_one(university_document)

# university_schema = {
#     "name": "string",
#     "location": "string",
#     "brief_info": "string",
#     "image_url": "string",
#     "university_logo": "string",
#     "university_website": "string",
#     "application_period": "string",
# }


# s3 = boto3.client('s3')
# bucket_name = 'wayabroad'

# # Checking files in the bucket
# response = s3.list_objects_v2(Bucket=bucket_name)
# for file in response['Contents']:
#     print(file['Key'])



# Trying smtplib to check if it works
import smtplib

# Email credentials
email = "habibullochutboev@gmail.com"
password = "qgls phyq fchv orvs"

# Email content
subject = "Test Email"
body = "This is a test email."
msg = f"Subject: {subject}\n\n{body}"

# Send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
server.sendmail(email, email, msg)
server.quit()



