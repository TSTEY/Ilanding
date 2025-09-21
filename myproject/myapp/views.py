from django.shortcuts import render,redirect,get_object_or_404
from .import models
from . import forms
from . import serializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

def index(request):
    header = models.Header.objects.all()
    block_one = models.BlockOne.objects.all()
    block_two = models.BlockTwo.objects.all()
    block_three = models.BlockThree.objects.all()
    block_four = models.BlockFour.objects.all()
    block_five = models.BlockFive.objects.all()
    block_six = models.BlockSix.objects.all()
    block_seven = models.BlockSeven.objects.all()
    block_eight = models.BlockEight.objects.all()
    block_nine = models.BlockNine.objects.all()
    block_ten = models.BlockTen.objects.all()
    footer = models.Footer.objects.all()
    
    body = {
        'header':header,
        'block_one':block_one,
        'block_two':block_two,
        'block_three':block_three,
        'block_four':block_four,
        'block_five':block_five,
        'block_six':block_six,
        'block_seven':block_seven,
        'block_eight':block_eight,
        'block_nine':block_nine,
        'block_ten':block_ten,
        'footer':footer,
        
    }
    return render(request,'index.html',body)

def service_details(request):
    return render(request,'service_details.html')

def starter_page(request):
    return render(request,'starter_page.html')

def admin(request):
    return render(request,'admin/admin.html')

def header(request):
    header = models.Header.objects.all()
    return render(request,'admin/header.html',{'header':header})

def block_one(request):
    block_one = models.BlockOne.objects.all()
    return render(request,'admin/Block/one.html',{'block_one':block_one})

def block_two(request):
    block_two = models.BlockTwo.objects.all()
    return render(request,'admin/Block/two.html',{'block_two':block_two})

def block_three(request):
    block_three = models.BlockThree.objects.all()
    return render(request,'admin/Block/three.html',{'block_three':block_three})

def block_four(request):
    block_four = models.BlockFour.objects.all()
    return render(request,'admin/Block/four.html',{'block_four':block_four})

def block_five(request):
    block_five = models.BlockFive.objects.all()
    return render(request,'admin/Block/five.html',{'block_five':block_five})

def block_six(request):
    block_six = models.BlockSix.objects.all()
    return render(request,'admin/Block/six.html',{'block_six':block_six})

def block_seven(request):
    block_seven = models.BlockSeven.objects.all()
    return render(request,'admin/Block/seven.html',{'block_seven':block_seven})

def block_eight(request):
    block_eight = models.BlockEight.objects.all()
    return render(request,'admin/Block/eight.html',{'block_eight':block_eight})

def block_nine(request):
    block_nine = models.BlockNine.objects.all()
    return render(request,'admin/Block/nine.html',{'block_nine':block_nine})

def block_ten(request):
    block_ten = models.BlockTen.objects.all()
    return render(request,'admin/Block/ten.html',{'block_ten':block_ten})

def footer(request):
    footer = models.Footer.objects.all()
    return render(request,'admin/footer.html',{'footer':footer})


# Header
def create_header(request):
    if request.method == 'POST':
        form = forms.HeaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('header')
    else:
        form = forms.HeaderForm()
    return render(request, 'admin/form.html',{'form':form})

def update_header(request,user_id):
    user = get_object_or_404(models.Header,id=user_id)
    if request.method == 'POST':
        form = forms.HeaderForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('header')
    else:
        form = forms.HeaderForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_header(request,user_id):
    user = get_object_or_404(models.Header,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('header')
    return render(request,'admin/delete.html',{'user':user})


# Block
# One
def create_block_one(request):
    if request.method == 'POST':
        form = forms.BlockOneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_one')
    else:
        form = forms.BlockOneForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_one(request,user_id):
    user = get_object_or_404(models.BlockOne,id=user_id)
    if request.method == 'POST':
        form = forms.BlockOneForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_one')
    else:
        form = forms.BlockOneForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_one(request,user_id):
    user = get_object_or_404(models.BlockOne,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_one')
    return render(request,'admin/delete.html',{'user':user})

# Two
def create_block_two(request):
    if request.method == 'POST':
        form = forms.BlockTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_two')
    else:
        form = forms.BlockTwoForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_two(request,user_id):
    user = get_object_or_404(models.BlockTwo,id=user_id)
    if request.method == 'POST':
        form = forms.BlockTwoForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_two')
    else:
        form = forms.BlockTwoForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_two(request,user_id):
    user = get_object_or_404(models.BlockTwo,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_two')
    return render(request,'admin/delete.html',{'user':user})

# Three
def create_block_three(request):
    if request.method == 'POST':
        form = forms.BlockThreeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_three')
    else:
        form = forms.BlockThreeForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_three(request,user_id):
    user = get_object_or_404(models.BlockThree,id=user_id)
    if request.method == 'POST':
        form = forms.BlockThreeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_three')
    else:
        form = forms.BlockThreeForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_three(request,user_id):
    user = get_object_or_404(models.BlockThree,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_three')
    return render(request,'admin/delete.html',{'user':user})

# Four
def create_block_four(request):
    if request.method == 'POST':
        form = forms.BlockFourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_four')
    else:
        form = forms.BlockFourForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_four(request,user_id):
    user = get_object_or_404(models.BlockFour,id=user_id)
    if request.method == 'POST':
        form = forms.BlockFourForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_four')
    else:
        form = forms.BlockFourForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_four(request,user_id):
    user = get_object_or_404(models.BlockFour,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_four')
    return render(request,'admin/delete.html',{'user':user})

# Five
def create_block_five(request):
    if request.method == 'POST':
        form = forms.BlockFiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_five')
    else:
        form = forms.BlockFiveForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_five(request,user_id):
    user = get_object_or_404(models.BlockFive,id=user_id)
    if request.method == 'POST':
        form = forms.BlockFiveForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_five')
    else:
        form = forms.BlockFiveForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_five(request,user_id):
    user = get_object_or_404(models.BlockFive,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_five')
    return render(request,'admin/delete.html',{'user':user})

# Six
def create_block_six(request):
    if request.method == 'POST':
        form = forms.BlockSixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_six')
    else:
        form = forms.BlockSixForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_six(request,user_id):
    user = get_object_or_404(models.BlockSix,id=user_id)
    if request.method == 'POST':
        form = forms.BlockSixForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_six')
    else:
        form = forms.BlockSixForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_six(request,user_id):
    user = get_object_or_404(models.BlockSix,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_six')
    return render(request,'admin/delete.html',{'user':user})

# Seven
def create_block_seven(request):
    if request.method == 'POST':
        form = forms.BlockSevenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_seven')
    else:
        form = forms.BlockSevenForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_seven(request,user_id):
    user = get_object_or_404(models.BlockSeven,id=user_id)
    if request.method == 'POST':
        form = forms.BlockSevenForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_seven')
    else:
        form = forms.BlockSevenForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_seven(request,user_id):
    user = get_object_or_404(models.BlockSeven,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_seven')
    return render(request,'admin/delete.html',{'user':user})

# Eight
def create_block_eight(request):
    if request.method == 'POST':
        form = forms.BlockEightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_eight')
    else:
        form = forms.BlockEightForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_eight(request,user_id):
    user = get_object_or_404(models.BlockEight,id=user_id)
    if request.method == 'POST':
        form = forms.BlockEightForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_eight')
    else:
        form = forms.BlockEightForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_eight(request,user_id):
    user = get_object_or_404(models.BlockEight,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_eight')
    return render(request,'admin/delete.html',{'user':user})

# Nine
def create_block_nine(request):
    if request.method == 'POST':
        form = forms.BlockNineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_nine')
    else:
        form = forms.BlockNineForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_nine(request,user_id):
    user = get_object_or_404(models.BlockNine,id=user_id)
    if request.method == 'POST':
        form = forms.BlockNineForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_nine')
    else:
        form = forms.BlockNineForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_nine(request,user_id):
    user = get_object_or_404(models.BlockNine,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_nine')
    return render(request,'admin/delete.html',{'user':user})

# Ten 
def create_block_ten(request):
    if request.method == 'POST':
        form = forms.BlockTenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('block_ten')
    else:
        form = forms.BlockTenForm()
    return render(request, 'admin/form.html',{'form':form})

def update_block_ten(request,user_id):
    user = get_object_or_404(models.BlockTen,id=user_id)
    if request.method == 'POST':
        form = forms.BlockTenForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('block_ten')
    else:
        form = forms.BlockTenForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_block_ten(request,user_id):
    user = get_object_or_404(models.BlockTen,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('block_ten')
    return render(request,'admin/delete.html',{'user':user})

# Footer
def create_footer(request):
    if request.method == 'POST':
        form = forms.FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('footer')
    else:
        form = forms.FooterForm()
    return render(request, 'admin/form.html',{'form':form})

def update_footer(request,user_id):
    user = get_object_or_404(models.Footer,id=user_id)
    if request.method == 'POST':
        form = forms.FooterForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('footer')
    else:
        form = forms.FooterForm()
    return render(request, 'admin/form.html',{'form':form})

def delete_footer(request,user_id):
    user = get_object_or_404(models.Footer,id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('footer')
    return render(request,'admin/delete.html',{'user':user})




# API
class HeaderAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.Header, id=head_id)
            serializers = serializer.HeaderSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.Header.objects.all()
        serializers = serializer.HeaderSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.HeaderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.Header, id=head_id)
        serializers = serializer.HeaderSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.Header, id=head_id)
        serializers = serializer.HeaderSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.Header, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockOneAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockOne, id=head_id)
            serializers = serializer.BlockOneSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockOne.objects.all()
        serializers = serializer.BlockOneSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockOneSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockOne, id=head_id)
        serializers = serializer.BlockOneSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockOne, id=head_id)
        serializers = serializer.BlockOneSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockOne, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockTwoAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockTwo, id=head_id)
            serializers = serializer.BlockTwoSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockTwo.objects.all()
        serializers = serializer.BlockTwoSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockTwoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockTwo, id=head_id)
        serializers = serializer.BlockTwoSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockTwo, id=head_id)
        serializers = serializer.BlockTwoSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockTwo, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockThreeAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockThree, id=head_id)
            serializers = serializer.BlockThreeSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockThree.objects.all()
        serializers = serializer.BlockThreeSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockThreeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockThree, id=head_id)
        serializers = serializer.BlockThreeSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockThree, id=head_id)
        serializers = serializer.BlockThreeSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockThree, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockFourAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockFour, id=head_id)
            serializers = serializer.BlockFourSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockFour.objects.all()
        serializers = serializer.BlockFourSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockFourSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockFour, id=head_id)
        serializers = serializer.BlockFourSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockFour, id=head_id)
        serializers = serializer.BlockFourSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockFour, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockFiveAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockFive, id=head_id)
            serializers = serializer.BlockFiveSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockFive.objects.all()
        serializers = serializer.BlockFiveSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockFiveSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockFive, id=head_id)
        serializers = serializer.BlockFiveSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockFive, id=head_id)
        serializers = serializer.BlockFiveSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockFive, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockSixAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockSix, id=head_id)
            serializers = serializer.BlockSixSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockSix.objects.all()
        serializers = serializer.BlockSixSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockSixSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockSix, id=head_id)
        serializers = serializer.BlockSixSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockSix, id=head_id)
        serializers = serializer.BlockSixSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockSix, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockSevenAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockSeven, id=head_id)
            serializers = serializer.BlockSevenSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockSeven.objects.all()
        serializers = serializer.BlockSevenSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockSevenSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockSeven, id=head_id)
        serializers = serializer.BlockSevenSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockSeven, id=head_id)
        serializers = serializer.BlockSevenSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockSeven, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockEightAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockEight, id=head_id)
            serializers = serializer.BlockEightSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockEight.objects.all()
        serializers = serializer.BlockEightSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockEightSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockEight, id=head_id)
        serializers = serializer.BlockEightSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockEight, id=head_id)
        serializers = serializer.BlockEightSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockEight, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockNineAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockNine, id=head_id)
            serializers = serializer.BlockNineSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockNine.objects.all()
        serializers = serializer.BlockNineSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockNineSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockNine, id=head_id)
        serializers = serializer.BlockNineSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockNine, id=head_id)
        serializers = serializer.BlockNineSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockNine, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class BlockTenAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.BlockTen, id=head_id)
            serializers = serializer.BlockTenSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.BlockTen.objects.all()
        serializers = serializer.BlockTenSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.BlockTenSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.BlockTen, id=head_id)
        serializers = serializer.BlockTenSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.BlockTen, id=head_id)
        serializers = serializer.BlockTenSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.BlockTen, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class FooterAPIView(APIView):
    def get(self, request, head_id=None):
        if head_id:
            head = get_object_or_404(models.Footer, id=head_id)
            serializers = serializer.FooterSerializer(head)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
        heads = models.Footer.objects.all()
        serializers = serializer.FooterSerializer(heads, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = serializer.FooterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        serializers = serializer.FooterSerializer(head, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        serializers = serializer.FooterSerializer(head, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, head_id):
        head = get_object_or_404(models.Footer, id=head_id)
        head.delete()
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationUserForm,CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request, user
            )
            return redirect('login')
    else:
        form = CustomUserCreationUserForm()
    return render(request,'login/register.html',{'form':form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')   
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('admin')
    else:
        form = CustomAuthenticationForm()
    return render(request,'login/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')



