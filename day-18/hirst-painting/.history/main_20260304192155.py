import colorgram




rgb_colors = []
colors = colorgram.extract("images.jpg",30)
for color in colors:
  r = color.rgb.r
  r = color.rgb.r
  r = color.rgb.r

  rgb_colors.append(color.rgb)


print(rgb_colors)




