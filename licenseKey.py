# Given a license key such as "2-4A0r7-4k".
# Add dashes every K character to create groups.
# The first group can have a smaller number of characters

def solution(licenseKey, K):
  licenseKey = licenseKey.replace("-","") # Removes the dashes
  S = list(licenseKey.upper()) # convert string to uppercase
  
  #Traverse backwards by K step starting at 0
  for i in range( len(licenseKey) - K, 0, -K ):
     licenseKey.insert(i, "-")
      
  licenseKey = "".join(licenseKey)
  
  return licenseKey

