# DeTox
[中文版](./README_CN.md)  
Unprotect images to train AI

### Abstract

The image detoxification tool is a groundbreaking technology designed to reverse-process obfuscated images and restore their original information. With the widespread application of artificial intelligence, image obfuscation techniques—such as adding subtle noise to images that does not significantly affect human visual perception but disrupts AI recognition and training—have emerged as potential threats. The development and application of image detoxification tools hold significant importance across multiple fields.

In the field of autonomous driving, image detoxification tools are crucial. Autonomous vehicles rely on image recognition technology to perceive their surroundings, determine driving routes, and identify obstacles or pedestrians. If the images fed into these systems are obfuscated or "poisoned," AI might fail to recognize them accurately, leading to traffic accidents and endangering lives. Image detoxification tools can detect and repair such toxic images, ensuring that the systems receive accurate environmental information, thereby enhancing the safety and reliability of autonomous driving.

In the realm of content safety, the potential applications of image detoxification are immense. On social media and online platforms, harmful information is being disseminated in increasingly covert ways. Malicious actors may use obfuscation techniques to bypass AI content moderation, spreading discriminatory, violent, or illegal information. This not only poses a threat to society but also undermines the reputation of these platforms. Image detoxification tools can eliminate these obfuscation elements, enabling moderation systems to accurately identify harmful content and ensuring a healthy and safe online environment.

Additionally, in the field of physical security, image detoxification is indispensable. For example, criminals may design clothing with specific patterns or noise to evade detection by security cameras or biometric systems. Such "toxic disguises" could challenge public safety. The application of image detoxification tools can effectively decode these obfuscation methods, allowing security systems to function properly and further enhancing the effectiveness of safety measures.

This repository introduces a simple yet effective combination of filters for detoxifying images.

### Known to work against

[Sanative](https://app.sanative.ai/shield)  
[Glaze](https://glaze.cs.uchicago.edu/what-is-glaze.html)  
[NightShade](https://github.com/Shawn-Shan/nightshade-release)  
[ArtShield](https://artshield.io/)  
And much more.  

### Sample
Original Picture  
![Original Picture](./or.png)  
Poisoned(Protected) Picture  
![Protected Picture](./pr.png)  
DeToxed Picture  
![DeToxed Picture](./done.png)  
StableDiffusion can describe the DeToxed picture(done.png) properly.  
<img width="1280" alt="image" src="https://github.com/user-attachments/assets/f716267c-7365-441e-9234-3dc2283b10a7">  
ChatGPT can describe it properly.  
<img width="848" alt="image" src="https://github.com/user-attachments/assets/ed7f02d7-c501-49fa-bf1d-bfe737684dfb">  
We omit many similar tests. In short, almost all use cases do not misinterpret DeToxed images, either for description, imitation, recognition or training.  
Even invited human testers said DeToxed images were better for viewing.  

### See Also
[DeWm](https://github.com/huzpsb/DeWm/)  
[Glaze and the Effectiveness](https://huggingface.co/blog/parsee-mizuhashi/glaze-and-anti-ai-methods)  
