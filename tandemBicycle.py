def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()

    if fastest:
        blueShirtSpeeds.sort(reverse=True)
        maxPossibleSpeed = 0
    else:
        blueShirtSpeeds.sort()
        minPossibleSpeed = 0

    speed = 0
    for idx in range(len(redShirtSpeeds)):
        speed += max(redShirtSpeeds[idx] , blueShirtSpeeds[idx])

    return speed


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, False))


