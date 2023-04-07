# workout-tracker
a natural language processing app that can count your calories by saying it `i ran for 5km` it will calculate estimated time and calories and it uses a `api` called `NutritionixAPI` and then it adds your data to google sheet 
![Screenshot from 2023-04-07 22-57-27](https://user-images.githubusercontent.com/62764033/230651405-80b69a11-7512-4e52-bcf7-5937e894c11e.png)  

using a `API` called `sheety - https://sheety.co/docs/requests`

# Installation 
frist you need to get hold of `Nutrutionix API id and Key` `https://developer.nutritionix.com/admin/access_details`  

![Screenshot from 2023-04-07 23-08-30](https://user-images.githubusercontent.com/62764033/230652968-aa1debf2-2769-4269-acfb-af63635792ad.png)  
 
then post your request using requests.post() method

to add your current workout data to google sheets you have to login to `sheety - https://sheety.co/docs/requests` and read their docs to know hot to send  a request and don't forget to enable `POST` method their website  
![Screenshot from 2023-04-07 23-14-40](https://user-images.githubusercontent.com/62764033/230653726-d36ee2da-583a-43a1-81a7-75340491ad81.png)

