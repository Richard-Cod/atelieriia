from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from base64 import b64encode




default_image_binary = "iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAMAAACahl6sAAAAM1BMVEX+///9/v74+fn3+Pjy8/Tu7+/t7u/p6urn6On6+/vs7e37/Pzx8vLq6+z19vbv8PH09fVYJh4NAAAEGklEQVR42u2dC3ajMAxFDRgscPjsf7UNbXPazkzaNOg9CY/vDt7RXzJJqFQqlUqlUnmEpu1i7Id3+hi7tgkno+nikOQfpCF2p1Ezxkm+ZYpjcE++zPIA8yUHz3SDPMzQBa8sX43xs1mW4JHuVcYvpfizSh7kKQZnsRLlWVIMfriZ4+xGaZMcIrXBBYscxkX6WkWBNZijosOBEiUd5krUdIiYpmGFOHcR8a2oYtbc5ySqzFYj1yDK9MGETdQxaYa1HWsnWTiXumMZVRPljHWD3z/OAmEIZFRLoaVJQAahmwQUITvcebEXGNTElQUHtZZEAcLsgmGhTu64RoHC8y2oZzF9axIotLzVCJY5kOgEDKsmgkOEFySQSeQzl8ABMBqaNI7I/uSNFCgAO19uSQRsT2ymK3jSYq2FgLMId6ENz74FCeF0W/AywiokgqcKqUJAVCFVCIgq5P8siIQWpZheqwrxNlgVMyFyhMAXjazlA2GLEiigd9jXzxkCB3hFZN2s4PmXk31DuAgYzlqLsGpkvQmEp63AQrBwel/CMZR151F9tmwZ68DHWtxbKPpmRbtOo9+icDbYhCBhHafhQcILEWwDzGp94ZWEV0XAfSOvimCfnpEeC+ATMGuogidgZvKFrlI4CxT84M72LJhvsT0LlrfongXKW8yGEVoTudUQN5SwqyFsT8fts4C9PGuh9ZVGvZRwO3hgKeEXEUy4U7/lQYa7RRGBhDtzWEdWd97KF3xgsKjqiAzMXDBCGy6r3Kudge1yr3JRZB1A0SaxNoiaSeyKobJJDIuhap9ibxClY7UDg6hEiQeDqESJC4MomMSHQRRM4sQgh03ixSB7E3zuoq708NS6y1K78rqJkNcoKSFCdkbvj5XxawjbCVdx5vXlWdfW8Yy7E9W85Spn7STvL0rB85W3WL8KOd+eVFWIP4uUEiPNuc6GgFPJFnzRn+0Aqj/t+moah/PdpPUvV44mxDGd9uamqUOSkxTcHj4kJtuzm0Z8+ImTrHJVuOYuW/dq4mG3+jCK4Z5uUX35kIykNJuqDCsp46rnVJ9ZqbHSbMDvR+aNtI/IC/xH6Ca8lhFpC9ZfDTbLqh7e34b+uugbpukuJFP8YZiL4h9aZiMRH2IULDOS3eke87o9HzNt7DG14tmY6WP7xB+YKjWD2gy/yWatD3e672YPGSZH1yretcT8k4zDzzFYrLkIGd9LUZySKNz5u9FsWvWeY8r6Ox0b/t4kLafUsW+S1F4uWDOi/7eNRcqcXz7AMyk9t7InluBYb851/LGVD1aF528+aPTW6bZs509Zb0wqz489kPW/irRhKSFn7axlhMg1SPC/VUhC6YMce9pyhJy8YbwRyxFSRPa95l+dzwjtGaoQZxQkRAqhCvFGFeKNKsQbL26/cd+lwF+LAAAAAElFTkSuQmCC"

class Profile(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE)
	description = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)
	avatar = models.ImageField(upload_to='avatars/',blank=True,default='avatars/no.png')
	genre = models.IntegerField(choices=((1, ("Homme")),
									    (2, ("Femme")))
								)
	binaire = models.TextField(default=default_image_binary,null=True)

	def __str__(self):
		return self.user.username
	

