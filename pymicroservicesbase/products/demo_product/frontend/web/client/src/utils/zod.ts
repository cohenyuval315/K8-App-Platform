import { z } from "zod";

/**
 * This function will remove the fields that are not valid according to the schema
 * @template T
 * @param {z.ZodType<T>} schema - The Zod schema to validate against.
 * @param {z.ZodObject} object - The object to parse against the schema.
 * @returns {Partial<T>} - The parsed and validated object with all fields optional.
 */
export const parseSchemaObject = (schema, object) => {
    try {
        return schema.parse(object);
    } catch (e) {
        if (!(e instanceof z.ZodError))
            throw new Error("Failed to parse object");

        const errorFields = e.errors.map((err) => err.path[0]);
        const fieldsToOmit = errorFields.reduce((obj, key) => {
            obj[key] = object[key];
            return obj;
        }, {});

        try {
            return schema.omit(fieldsToOmit).parse(object);
        } catch {
            throw new Error("Failed to parse object");
        }
    }
  };
