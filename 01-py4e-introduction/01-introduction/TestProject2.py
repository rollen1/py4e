#Self assesment of the Big 5 Personality traits
print("Only rate everything from 1 to 5, a maximum of 25 points for each trait")
print("1 = completely disagree, 5 = completely agree")

#Openness
o1 = int(input('I have a rich vocabulary: '))
o2 = int(input('I have a vivid imagination: '))
o3 = int(input('I generate excellent ideas: '))
o4 = int(input('I am quick to understand things: '))
o5 = int(input('I often spend time reflecting on things: '))
o = o1 + o2 + o3 + o4 + o5
#Conscientiousness
c1 = int(input('I am always prepared: '))
c2 = int(input('I pay attention to details: '))
c3 = int(input('I get chores done right away: '))
c4 = int(input('I like to plan my day: '))
c5 = int(input('I like my room clean and I know where I leave my things: '))
c = c1 + c2 + c3 + c4 + c5
#Extraversion
e1 = int(input('I am the life of the party: '))
e2 = int(input('I feel comfortable around people: '))
e3 = int(input('I start conversations: '))
e4 = int(input('I dont mind being the center of attention: '))
e5 = int(input('I recharge energy from socializing: '))
e = e1 + e2 + e3 + e4 + e5
#Agreeableness
a1 = int(input('I am interested in people: '))
a2 = int(input('I sympathize with others feelings: '))
a3 = int(input('I find it hard to say no: '))
a4 = int(input('I sometimes prioritize others needs over my own: '))
a5 = int(input('Friends describe me as caring with a soft heart: '))
a = a1 + a2 + a3 + a4 + a5
#Neuroticism
n1 = int(input('I get stressed out easily: '))
n2 = int(input('I often get depressed: '))
n3 = int(input('I have frequent mood swings: '))
n4 = int(input('I worry about things other people dont worry as much about: '))
n5 = int(input('I get irritated, angry easily: '))
n = n1 + n2 + n3 + n4 + n5

#Prints self-assessed values

print('Openness: ', o)
print('Individuals who score high on Openness are creative and open to new experiences. Low scorers tend to be traditional and conventional.')

print('Conscientiousness: ', c)
print('Individuals who score high on Conscientiousness are careful and diligent. Low scorers are impulsive and disorganized.')

print('Extraversion: ', e)
print('Individuals who score high on Extraversion are outgoing and social. Individuals who score low tend to be shut ins.')

print('Agreeableness: ', a)
print('Individuals who score high on Agreeableness are empathetic and tend to be people pleasers. Low scorers are critical and assertive.')

print('Neuroticism: ', n)
print('Individuals who score high on Neuroticism are anxious, moody and they can perceive minor situations as hopelessly difficult. Low scorers tend not to be so reactive emotionally and are more calm.')
