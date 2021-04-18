function base api view এ decorator ব্যবহার করে operation define করা হয়। 

আর request.method == decorator এর parameter operation define করা হয়। 

non-primary key base operation গুলোতে [GET,POST] আর primary key base operation গুলো [GET, PUT, DELETE] ব্যবহার করলে ই চলে । 

` from rest_framework.decorators import api_view `

api_view class ব্যবহার হয়। 

এই project এ আমরা student information add এবং specific student এর info UPDATE বা DELETE করতে পারব। 

