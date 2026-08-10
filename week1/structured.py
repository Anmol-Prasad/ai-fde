from pydantic import BaseModel

# Extending BaseModel means that class is a pydantic model 
class Contact(BaseModel):
    name: str
    email: str | None = None
    company: str | None = None

contact = Contact(
    name="Don Critioli",
    email="doncristioli@acme.co",
    company="Acme"
)

schema = Contact.model_json_schema()

