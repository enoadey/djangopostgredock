from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.models import data_view

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from django.template import loader
from myapp.apps import MyappConfig
import pandas as pd
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
class DataViews(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def index(request):
        con = str(data_view.objects.all().query)
        df = pd.read_sql_query(con, connection)
        total_rows = len(df.index)
        bien = total_rows + 1
        json_records = df.reset_index().to_json(orient ='records')
        data = []
        data = json.loads(json_records)
        s = df.groupby('ville')['prix_m2_ttc'].mean()
        mean_records = s.reset_index().to_json(orient ='records')
        mean = []
        mean = json.loads(mean_records)
        st = df.groupby('ville')['prix_m2_ttc'].std()
        std_records = st.reset_index().to_json(orient ='records')
        std = []
        std = json.loads(std_records)
        return render(request, 'data/index.html',{'df': data,'bien':bien, 'mean':mean, 'std':std})
def std(request, format=None):
        con = str(data_view.objects.all().query)
        df = pd.read_sql_query(con, connection)
        s = df.groupby('ville')['prix_m2_ttc'].mean()
        mean_records = s.reset_index().to_json(orient ='records')
        mean = []
        mean = json.loads(mean_records)
        return Response({"mean":mean}, status=status.HTTP_200_OK)

