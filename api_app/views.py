from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serialisers import UserSerializer,CourSerializer,ArchiveUserSerializer,ArchiveCourSerializer
from .models import  User,ArchiveUser,ArchiveCour,Cour

from rest_framework_simplejwt.views import(
TokenObtainPairView,
TokenRefreshView,
)

class NewTokenObtainPairView(TokenObtainPairView):
     permission_classes = (IsAuthenticated,)

class NewTokenRefreshView(TokenRefreshView):
     permission_classes = (IsAuthenticated,)


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



class UserViews(APIView):
    

    def post(self, request):
        
        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":
                serializer = UserSerializer(data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "error", "data": "Role insuffisant"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, id = None):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

           # if user_login.role == "admin":
            if id:
                item = User.objects.filter(id=id)
                if item:
                    serializer = UserSerializer(item, many=True)
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                
                return Response({"status": "error", "data": "Utilisateur n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)



            query_set = User.objects.all()
            serializer = UserSerializer( query_set, many=True)
            return Response(serializer.data)
            #return Response({"status": "failed", "data": "role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_404_NOT_FOUND)
   
           

    def patch(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            #if user_login.role == "admin":

            if id:
                item = User.objects.get(id=id)
                serializer = UserSerializer(item, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data})
                else:
                    return Response({"status": "error", "data": serializer.errors})

            return Response({"status": "failed", "data": "Utilisateur n'existe pas"}, status=status.HTTP_401_UNAUTHORIZED)

            #return Response({"status": "failed", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)



    
    
    def delete(self, request, id):
        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":
                if id:
                    item = get_object_or_404(User, id=id)
                    item.delete()

                    return Response({"status": "success", "data": "Utilisateur supprimé"})

                return Response({"status": "error", "data": "Utilisateur n'existe pas"})

            return Response({"status": "error", "data": "Role insuffisant"})

        return Response({"status": "success", "data": "Connexion requise"})




class Getlogger(APIView):

        def get(self, request):
            if request.user.id:
                user_id = request.user.id
                user_login = User.objects.get(id = user_id)

                serializer = UserSerializer(user_login, read_only= True)  
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  

            return Response({"status": "error", "data": "Veillez vous connecté"})  




class CourAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CourSerializer

    def get_object(self):
        return self.request.data



class CourViews(APIView):
    

    def post(self, request):
        
       if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :

                serializer = CourSerializer(data=request.data)
                
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "error", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)



    def get(self, request, id = None):

       if  request.user.id:

            if id:
                item = Cour.objects.filter(id=id)
                if item:
                    serializer = CourSerializer(item, many=True)
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                
                return Response({"status": "error", "data": "Cour n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)



            query_set = Cour.objects.all()
            serializer = CourSerializer( query_set, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

            
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_404_NOT_FOUND)



    def patch(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":

                if id:
                    item = Cour.objects.get(id=id)
                    serializer = CourSerializer(item, data=request.data, partial=True)

                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "success", "data": serializer.data,"msg":"ca marche"})
                    else:
                        return Response({"status": "error", "data": serializer.errors})

                return Response({"status": "failed", "data": "Utilisateur n'existe pas"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"status": "failed", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)


    
    def delete(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :
                if id:
                    item = get_object_or_404(Cour, id=id)
                    item.delete()

                    return Response({"status": "success", "data": "Cour supprimé"})

                return Response({"status": "error", "data": "Cour n'existe pas"})

            return Response({"status": "error", "data": "Role insuffisant"})

        return Response({"status": "success", "data": "Connexion requise"})





class ArchiveUserViews(APIView):
    

    def post(self, request):
        
       if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":
                serializer = ArchiveUserSerializer(data= request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "error", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)



    def get(self, request, id = None):

       if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            #if user_login.role == "admin" :
            if id:
                item = ArchiveUser.objects.filter(id=id)
                if item:
                    serializer = ArchiveUserSerializer(item, many=True)
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                
                return Response({"status": "error", "data": "Archive n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)



            query_set = ArchiveUser.objects.all()
            serializer = ArchiveUserSerializer( query_set, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            #return Response({"status": "failed", "data": "role insuffisant"}, status=status.HTTP_403_FORBIDDEN)
            
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_401_UNAUTHORIZED)



    def patch(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :

                if id:
                    item = ArchiveUser.objects.get(id=id)
                    serializer = ArchiveUserSerializer(item, data=request.data, partial=True)

                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "success", "data": serializer.data})
                    else:
                        return Response({"status": "error", "data": serializer.errors})

                return Response({"status": "failed", "data": "Utilisateur n'existe pas"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"status": "failed", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)


    
    def delete(self, request, id):

        if  request.user.id:
            if id:
                user_id = request.user.id
                user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":
                if id:
                    item = get_object_or_404(ArchiveUser, id=id)
                    idUser = item.user
                    userArchive = User.objects.get(id = idUser)
                    item.delete()
                    userArchive.delete()

                    return Response({"status": "success", "data": "Archive supprimé"})

                return Response({"status": "error", "data": "Archive n'existe pas"})

            return Response({"status": "error", "data": "Role insuffisant"})

        return Response({"status": "success", "data": "Connexion requise"})




class ArchiveCourViews(APIView):
    

    def post(self, request):
        
       if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :

                serializer = ArchiveCourSerializer(data=request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "error", "data": "Role insuffisant"}, status=status.HTTP_400_BAD_REQUEST)
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, id = None):

       if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :
                if id:
                    item = ArchiveCour.objects.filter(id=id)
                    if item:
                        serializer = ArchiveCourSerializer(item, many=True)
                        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                    
                    return Response({"status": "error", "data": "Archive n'existe pas"}, status=status.HTTP_400_BAD_REQUEST)



                query_set = ArchiveCour.objects.all()
                serializer = ArchiveCourSerializer( query_set, many=True)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"status": "failed", "data": "role insuffisant"}, status=status.HTTP_403_FORBIDDEN)
            
       return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_401_UNAUTHORIZED)



    def patch(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :

                if id:
                    item = ArchiveCour.objects.get(id=id)
                    serializer = ArchiveCourSerializer(item, data=request.data, partial=True)

                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "success", "data": serializer.data})
                    else:
                        return Response({"status": "error", "data": serializer.errors})

                return Response({"status": "failed", "data": "Utilisateur n'existe pas"}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({"status": "failed", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN)

    
    
    def delete(self, request, id):
        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin" :
                if id:
                    item = get_object_or_404(Cour, id=id)
                    item.delete()

                    return Response({"status": "success", "data": "Archive supprimé"})

                return Response({"status": "error", "data": "Archive n'existe pas"})

            return Response({"status": "error", "data": "Role insuffisant"})

        return Response({"status": "error", "data": "Connexion requise"})   



class ArchiveUserDataViews(APIView):

    def post(self, request):
            if request.user.id:
                user_id = request.user.id
                user_login = User.objects.get(id = user_id) 
                if user_login.role == "admin":
                    serializer = ArchiveUserSerializer(data= request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                    else:
                        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                return Response({"status": "error", "data": "Role insuffisant"}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({"status": "error", "data": "Connexion requise"}, status=status.HTTP_403_FORBIDDEN) 
            
    def delete(self, request, id):

        if  request.user.id:
            user_id = request.user.id
            user_login = User.objects.get(id = user_id)

            if user_login.role == "admin":
                
                if id:
                    item = ArchiveUser.objects.get(id=id)
                    userArchive = User.objects.get(id = item.user_id)
                    item.delete()
                    userArchive.delete()

                    return Response({"status": "success", "data": "Archive supprimé"})

                return Response({"status": "error", "data": "Archive n'existe pas"})

            return Response({"status": "error", "data": "Role insuffisant"})

        return Response({"status": "error", "data": "Connexion requise"})
        
        

def UserArchive(id):
    if id:
        user_login = User.objects.get(id = id) 
        user_login.is_archive = True
        user_login.save()
