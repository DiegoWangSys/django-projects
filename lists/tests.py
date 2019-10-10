from django.test import TestCase
from lists.models import Item

#from django.urls import resolve
#from django.http import HttpRequest
#from lists.views import home_page
#from django.template.loader import render_to_string
#views aims to handle url

# Create your tests here.
class HomePageTest(TestCase):
    
    

    def test_uses_home_template(self):
       
        response=self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    
    def test_can_save_a_POST_request(self):
        self.client.post('/',data={'item_text':"A new list item"})
        #we wish here we could save the message in our database
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')
    
    def test_redirects_after_POST(self):
        response=self.client.post('/',data={'item_text':"A new list item"})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'/')
        #here we make sure we use the home.html to handle the POST request
        #but we need to redirect POST request
        
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)
        
    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response=self.client.get('/')
        self.assertIn('itemey 1',response.content.decode())
        self.assertIn('itemey 2',response.content.decode())



class ItemModelTest(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item=Item()
        first_item.text='The first (ever) list item'
        first_item.save()
        #we have an item and save it
        
        second_item=Item()
        second_item.text='Item the second'
        second_item.save()
        #we have a second item and save it too
        
        saved_items=Item.objects.all()
        #we retrieve all the saved items
        self.assertEqual(saved_items.count(),2)
        first_saved_item=saved_items[0]
        second_saved_item=saved_items[1]
        self.assertEqual(first_saved_item.text,'The first (ever) list item')
        self.assertEqual(second_saved_item.text,'Item the second')
        
        


