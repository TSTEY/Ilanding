from rest_framework import serializers
from . import models

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Header
        fields = '__all__'
        
class BlockOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockOne
        fields = '__all__'
        
class BlockTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockTwo
        fields = '__all__'
        
class BlockThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockThree
        fields = '__all__'
        
class BlockFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockFour
        fields = '__all__'
        
class BlockFiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockFive
        fields = '__all__'
        
class BlockSixSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockSix
        fields = '__all__'
        
class BlockSevenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockSeven
        fields = '__all__'
        
class BlockEightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockEight
        fields = '__all__'
        
class BlockNineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockNine
        fields = '__all__'
        
class BlockTenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlockTen
        fields = '__all__'
        
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Footer
        fields = '__all__'
        
