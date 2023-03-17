##################################################################################################################
#                
#                           Email Parser : Sends Features to CSV or print
#
##################################################################################################################

# import modules
import os
import csv
from email.parser import BytesParser, Parser
from email.policy import default


def send_email_features_to_csv(folder):
    with open('email_features.csv', 'w', newline='') as fp:
        writer = csv.writer(fp)
        
        # header row
        writer.writerow(["Subject", "To", "From", "Date", "CC", "BCC", "Message ID", 
                     "In Reply To", "References", "Reply To", "Sender", "Received", 
                     "Content Type", "Content Encoding", "Content Disposition", "Body", "Body Length"])
        
        # define max & count
        max = 19000
        count = 0
        for filename in os.listdir(folder):
            try:
                if ((count < max) and filename.endswith('.txt')):
                    # read each file as binary 
                    with open(os.path.join(folder, filename), 'rb') as fp:

                        # define message object
                        msg = BytesParser(policy=default).parse(fp)

                        # parse features
                        subject_ = msg.get('subject')
                        to_ = msg.get('to')
                        from_ = msg.get('from')
                        date_ = msg.get('date')

                        cc_ = msg.get('cc')
                        bcc_ = msg.get('bcc')
                        message_id_ = msg.get('message-id')
                        in_reply_to_ = msg.get('in-reply-to')

                        references_ = msg.get('references')
                        reply_to_ = msg.get('reply-to')
                        sender_ = msg.get('sender')
                        received_ = msg.get('received')

                        content_type_ = msg.get('content-type')
                        content_encoding_ = msg.get('content-encoding')
                        content_disposition_ = msg.get('content-disposition')
                        
                        # msg = BytesParser(policy=default).parse(fp)
                        body_ = msg.get_body(preferencelist=('plain')).get_content()
                        body_length_ = len(body_)

                        # Write the row to the csv file
                        writer.writerow([subject_, to_, from_, date_, cc_, bcc_, 
                                         message_id_, in_reply_to_, references_, 
                                         reply_to_, sender_, received_, content_type_, 
                                         content_encoding_, content_disposition_, body_, body_length_])
                        count+=1
            except:
                pass
