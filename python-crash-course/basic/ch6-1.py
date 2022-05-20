alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
new_points = alien_0['points']
print(f"You just earned {new_points} points.")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

del alien_0['color']
print(alien_0)

point_value = alien_0.get('points')
print(point_value)
color_value = alien_0.get('color')
print(color_value)
color_value = alien_0.get('color', 'No color value')
print(color_value)