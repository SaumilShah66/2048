import pyautogui
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pyxhook
import pickle
# [1,0,0,0] for Up
# [0,1,0,0] for Down
# [0,0,1,0] for Right
# [0,0,0,1] for Left
i = 0
keys = []
def OnKeyPress(event):
  # fob=open(log_file,'a')
  # fob.write(event.Key)
  # fob.write('\n')
  global i
  global keys
  if event.Key=='Up':
  	l = [1,0,0,0]
  if event.Key=='Down':
  	l = [0,1,0,0]
  if event.Key=='Right':
  	l = [0,0,1,0]
  if event.Key=='Left':
  	l = [0,0,0,1]	
  if event.Ascii==96: 
    new_hook.cancel()
    print(len(keys))
    pickle.dump(keys,open('keys_2.p','w'))
    
  print(l)
  im = np.array(pyautogui.screenshot(region=(485,270,445,445)))
  im = cv2.cvtColor(im,cv2.COLOR_RGB2BGR)
  keys.append(l)
  i = i+1
  cv2.imwrite('images/images_2/%s.jpg'%i,im)
  print("saved")



new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()

