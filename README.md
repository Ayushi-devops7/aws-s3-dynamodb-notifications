# AWS S3 to DynamoDB Automation with Real-Time Notifications

**Excited to Share My Latest AWS Project!**   
This project integrates several AWS services to automate data storage and send real-time notifications.

## **Project Overview**

This project uses AWS services to build an event-driven system that automates the storage of data uploaded to an S3 bucket and sends real-time notifications via SNS.

### **Architecture**
- **S3 Bucket**: Captures file uploads and triggers notifications.
- **SQS Queue**: Receives notifications from S3 for processing.
- **Lambda Function**: Processes SQS messages, stores data in DynamoDB, and triggers SNS notifications.
- **DynamoDB**: Stores metadata of uploaded objects.
- **SNS Topic**: Sends SMS notifications for successful operations.

---

## **Steps to Create the Project**

### **Step 1: Create an S3 Bucket**
1. **Log in to AWS Console** and navigate to S3.
2. Click on **Create Bucket** and provide a unique bucket name (e.g., `my-s3-bucket-for-upload`).
3. Choose a region, set the permissions as required, and click **Create**.

---

### **Step 2: Configure S3 Event Notifications**
1. Go to your created S3 bucket and navigate to the **Properties** tab.
2. Under the **Event notifications** section, click **Create event notification**.
3. Choose an event type, such as `All object create events`.
4. Select **Send to SQS queue**, and create an SQS queue or select an existing one to capture the notifications.

---

### **Step 3: Set Up an SQS Queue**
1. Navigate to the **SQS** service in AWS.
2. Click on **Create Queue**.
3. Choose a standard queue and give it a name (e.g., `my-sqs-queue`).
4. Keep the default settings for now, and click **Create Queue**.
5. Note the Queue ARN, which will be used in the Lambda function.

---

### **Step 4: Create a Lambda Function**
1. Go to **Lambda** in AWS Console and click on **Create function**.
2. Select **Author from scratch** and provide a function name (e.g., `process-sqs-messages`).
3. Choose the runtime as **Node.js** or **Python**, depending on your preference.
4. Set up the Lambda execution role with permissions to:
   - Read from SQS
   - Write to DynamoDB
   - Publish SNS notifications
   - 
---

## **Step 4: Create a Lambda Function**
1. Navigate to **Lambda** in the AWS Console and click on **Create Function**.
2. Choose **Author from Scratch**, give your function a name, and select the desired runtime (e.g., Python or Node.js).
3. Attach an execution role with necessary permissions to interact with SQS, DynamoDB, and SNS.
4. Write your Lambda function to:
   - Process SQS messages.
   - Store data in DynamoDB.
   - Publish notifications to SNS.
5. Save and deploy the function.
6. Configure the Lambda trigger to process messages from the SQS queue.

---

## **Step 5: Set Up DynamoDB Table**
1. Navigate to **DynamoDB** in the AWS Console.
2. Click on **Create Table** and provide a table name (e.g., `ProcessedData`).
3. Set the **Primary Key** (e.g., `objectKey`) and adjust read/write capacity settings as needed.
4. Enable auto-scaling for better performance and scalability.

---

## **Step 6: Create an SNS Topic for Notifications**
1. Navigate to **SNS** in the AWS Console and click on **Create Topic**.
2. Choose the topic type as **Standard** and provide a name (e.g., `S3DataProcessingNotifications`).
3. After creating the topic, set up a subscription:
   - Select **SMS** as the protocol or email.
   - Enter the phone number where notifications should be sent.
4. Confirm the subscription and test by publishing a message.

---

## **Step 7: Connect All Services**
1. Configure the S3 bucket to send event notifications to the SQS queue.
2. Ensure the Lambda function is triggered by messages from the SQS queue.
3. Verify that the Lambda function:
   - Stores metadata in the DynamoDB table.
   - Triggers the SNS topic to send SMS notifications.
4. Test the entire workflow by uploading a file to the S3 bucket and checking the results.

---

## **Key Features**
- **Conditional Logic**: Notifications are only sent after data is successfully stored in DynamoDB.
- **Real-Time Notifications**: SMS alerts provide instant confirmation for data processing and storage.
- **Scalable and Reliable**: Leverages AWS services for efficient and scalable cloud-based automation.

---

## **What I Learned**
- **AWS Service Integration**: Seamlessly connecting S3, SQS, Lambda, DynamoDB, and SNS.
- **Data Integrity**: Ensuring accurate notifications through conditional logic.
- **Automation and Scalability**: Utilizing AWS tools to build a robust, automated workflow.
- **Real-Time Alerts**: Sending instant notifications for better monitoring and response.

---

## **Conclusion**
This project demonstrates the power of AWS services to build an event-driven, automated workflow. From S3 uploads to real-time notifications, every step showcases efficient cloud resource management. Feedback and suggestions are always welcome! 

