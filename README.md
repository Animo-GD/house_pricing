# To run this app
### Download The Model
- [house_pricing_model](https://drive.google.com/file/d/17NmKGmo6r2TuPR5YY3CgWrMQIBSEWphp/view?usp=sharing)
- Place the model in app/models
### Create Virtual Environment
```bash
python3 -m venv .housePricing
```
### Pull the image
```bash
docker pull moaazsoliman/house_pricing
```

### Run the image
```bash
docker run -p 8000:8000 moaazsoliman/house_pricing
```

### Follow the link: [localhost](http://localhost:8000/)
