from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from django.shortcuts import render


@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save() # This triggers the post_save signal
            return redirect('tweet:create')
    else:
        form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form': form})

def index(request):
    return render(request, 'tweet/index.html')