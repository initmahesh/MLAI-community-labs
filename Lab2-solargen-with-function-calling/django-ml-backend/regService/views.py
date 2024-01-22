
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dotenv import load_dotenv

from research.experiments.OpenAI_function_Call.OpenAI_SolarGen import gen_answer

load_dotenv()

@api_view(['GET','POST'])
def functioncall(request):
    query = request.data["message"]
    result = gen_answer(query)
    return Response({"response":result})



