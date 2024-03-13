from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class login(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")


def index(request):
    if request.method == "POST":
        form = login(request.POST)
        if form.is_valid():
            person = Person(form.cleaned_data['username'], form.cleaned_data['password'])
            people.append(person)
        else:
            return render(request, r"D:\myproject\lab5part2\templates\lab5\add.html", {
                "form": form
            })
    return render(request, r"D:\myproject\lab5part2\templates\lab5\add.html", {
        "form": login()
    })

def main(request):
    return render(request, r"D:\myproject\lab5part2\templates\lab5\main.html", {
        "peoples": people
    })


class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

people = []