import jsonSchema


{
  "type": "object",
  "properties": {
    "name": {"type": "string", // тут не хватает пары ключ: значение, допиши ее},
    "email": {"type": "string"},
    "age": {"type": "number", // тут не хватает пары ключ: значение, допиши ее}
  },
  "required": [ "name", "email", "age" ]
}