# code to check which keys were pressed by the user
for event in pygame.event.get():
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_w:
			print("Player moved up!")
		elif event.key == pygame.K_a:
			print("Player moved left!")
		elif event.key == pygame.K_s:
			print("Player moved down!")
		elif event.key == pygame.K_d:
			print("Player moved right!")