import colorgram




rgb_colors = []
colors = colorgram.extract("images.jpg",30)
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r,g,b)
  
  rgb_colors.append(color.rgb)


print(rgb_colors)




