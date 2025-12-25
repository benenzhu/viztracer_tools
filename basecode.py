from viztracer import VizTracer




tracer = VizTracer()
tracer.start()

def real_func():
    print(3)
    pass


def ignore_func():
    print(2)
    real_func()
    

def main(): 
    print(1)
    ignore_func()
    
main()


tracer.stop()
tracer.save() # als
