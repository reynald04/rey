import turtle as tt
  
  
tt.speed('fastest')
tt.rt(-90)
angle = 30
  

def y(sz, level):   
  
    if level > 0:
        tt.colormode(255)
          
        
        tt.pencolor(0, 255//level, 0)
         
        tt.fd(sz)
  
        tt.rt(angle)
  
        
        y(0.8 * sz, level-1)
          
        tt.pencolor(0, 255//level, 0)
          
        tt.lt( 2 * angle )
  
       
        y(0.8 * sz, level-1)
          
        tt.pencolor(0, 255//level, 0)
          
        tt.rt(angle)
        tt.fd(-sz)
y(80, 7)
tt.done()