
import re


pattern = r'^[tTmM][A-Za-z]{0,}'

paragraph="Diffusion refers to the process by which molecules intermingle as a result of their \
    kinetic energy of random motion. Consider two containers of gas A and B separated by a \
    partition. The molecules of both gases are in constant motion and make numerous collisions\
    with the partition. If the partition is removed as in the lower illustration, the gases will\
    mix because of the random velocities of their molecules. In time a uniform mixture of A and B\
    molecules will be produced in the container. The tendency toward diffusion is very strong even\
    at room temperature because of the high molecular velocities associated with the thermal\
    energy of the particles.".split()

words=[] 

for word in paragraph:
    if re.match (pattern,word):
        words.append(word)
        
print(words)
