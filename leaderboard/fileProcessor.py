import json, os
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import Leaderboard



def handle_uploaded_file(file):

    if not file.content_type.find('json') == -1 or not file.content_type.find('csv') == -1:
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)

        try:
            Leaderboard.objects.all().delete()
            result = []
            if file.content_type.find('csv') == -1:
                input_file=open('media/%s'%file.name, 'r')
                json_decode=json.load(input_file)
                
                for item in json_decode["scores"]:
                    # my_dict={}
                    # my_dict['fullname']=item.get('fullname')
                    # my_dict['username']=item.get('username')
                    # my_dict['email']=item.get('email')
                    # my_dict['point']=item.get('point')
                    my_dict = Leaderboard()
                    my_dict.fullname=item.get('fullname')
                    my_dict.username=item.get('username')
                    my_dict.email=item.get('email')
                    my_dict.points=item.get('point')
                    my_dict.save()
            else:
                data = pd.read_csv('media/%s'%file.name)
                for item in data.values.tolist():
                    my_dict=Leaderboard()
                    my_dict.fullname=item[0]
                    my_dict.username=item[1]
                    my_dict.email=item[2]
                    my_dict.points=item[3]
                    my_dict.save()

            # sorted_obj = {"scores": result}
            # sorted_obj['scores'] = sorted(sorted_obj['scores'], key=lambda x : x['point'], reverse=True)

            os.remove('media/%s'%file.name)
            return True
        except Exception as e:
            os.remove('media/%s'%file.name)
            print(e)
            print("File format did not meet requirement")
    else:
        return False


