from django.shortcuts import render, redirect
import threading
import time
import webbrowser

global_stop_flag = False
global_thread = None

def open_url_in_loop(url, timee):
    global global_stop_flag
    print(url, timee)
    while not global_stop_flag:
        webbrowser.open(url)
        print("OK 202")
        time.sleep(timee * 3600)

def sitechecker(request):
    global global_stop_flag, global_thread

    if request.method == 'GET' and 'url' in request.GET and 'time' in request.GET:
        url = request.GET['url']
        timee = float(request.GET['time'])

        global_stop_flag = False

        global_thread = threading.Thread(target=open_url_in_loop, args=(url, timee))
        global_thread.start()

        msg = f"{url} manzilga har {timee} soatda kirilib tursin!"
        return render(request, 'index.html', {'msg': msg})

    elif request.method == 'GET' and 'q' in request.GET and request.GET['q'] == 'stop':
        global_stop_flag = True
        if global_thread:
            global_thread.join()
        return redirect('/')

    return render(request, 'index.html', {'msg': ''})
