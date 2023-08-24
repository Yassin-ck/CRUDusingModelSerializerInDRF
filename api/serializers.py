from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only = True)
    def start_with_s(value):
        if value[0].lower() !='s':
            raise serializers.ValidationError('Name Should be start with S')
        
    name = serializers.CharField(validators = [start_with_s])
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only':True}}
        
     
    # field level validation    
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full !!!')
        return value
    
    
    # object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'sugiyan' and city.lower() != 'calicut':
            raise serializers.ValidationError('City should be Calicut')
        return data