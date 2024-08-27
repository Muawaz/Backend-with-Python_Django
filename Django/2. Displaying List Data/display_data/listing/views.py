from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Let's Explore Kumrat Valley",
        "content": "Kumrat Valley is a stunning destination located near Swat, surrounded by towering mountains and lush greenery. It's known for its crystal-clear rivers, majestic forests, and serene ambiance, making it a perfect spot for nature lovers and adventure seekers."
    },
    {
        "id": 2,
        "title": "The Enchanting Fairy Meadows",
        "content": "Fairy Meadows offers breathtaking views of Nanga Parbat, the 9th highest mountain in the world. This magical place is a haven for trekkers and photographers, with its lush meadows, starry nights, and mesmerizing landscapes."
    },
    {
        "id": 3,
        "title": "Discovering Hunza Valley",
        "content": "Hunza Valley, known for its vibrant culture and rich history, is a paradise on earth. The valley is famous for its apricot blossoms, stunning glaciers, and the warm hospitality of the Hunza people."
    },
    {
        "id": 4,
        "title": "The Serenity of Skardu",
        "content": "Skardu is a gateway to some of the world's highest peaks, including K2. The region is known for its peaceful lakes, rugged landscapes, and rich cultural heritage, making it a must-visit destination for adventure enthusiasts."
    },
    {
        "id": 5,
        "title": "Exploring the Beauty of Neelum Valley",
        "content": "Neelum Valley, with its cascading waterfalls, lush green meadows, and clear blue rivers, is one of Pakistan's most picturesque destinations. It's a perfect getaway for those seeking tranquility and natural beauty."
    }
]

def listing_view(request):
    
    return render(request, 'home.html', {'posts': posts})



from django.shortcuts import get_list_or_404

def listing_detail_view(request, post_id):
    for post in posts:
        if(post['id'] == post_id):
            return render(request, 'details.html', {'post': post})
        elif(post["id"] is None):
            return render(request, '404.html')
    


