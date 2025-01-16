"use client"
import { useState } from "react";
import { z } from "zod";

// Recursive fields example
const profileFields = [
  {
    type: "children",
    title: "Profile Information",
    description: "User's personal details",
    enabled: true,
    fields: [
      { type: "text", title: "First Name", description: "User's first name", enabled: true, value: "John" },
      { type: "text", title: "Last Name", description: "User's last name", enabled: true, value: "Doe" },
      { type: "email", title: "Email", description: "User's email address", enabled: true, value: "john.doe@example.com" },
    ]
  },
  { type: "tel", title: "Phone Number", description: "User's contact number", enabled: true, value: "+1 234 567 890" },
  { type: "text", title: "Username", description: "User's unique username", enabled: true, value: "johndoe123" },
  { type: "boolean", title: "Verified", description: "Indicates if the user's email is verified", enabled: true, value: true },
];

const validationSchema = z.object({
  firstName: z.string().min(1, { message: "First Name is required" }),
  lastName: z.string().min(1, { message: "Last Name is required" }),
  email: z.string().email({ message: "Invalid email format" }),
  phoneNumber: z.string().min(10, { message: "Phone number must be at least 10 digits" }),
  username: z.string().min(1, { message: "Username is required" }),
  verified: z.boolean(),
});

const ProfileForm = () => {
  const [formData, setFormData] = useState<any>(profileFields);
  const [isEditing, setIsEditing] = useState(false);
  const [activeField, setActiveField] = useState<any>(null);
  const [errors, setErrors] = useState<any>({});

  const handleChange = (field: string, value: any) => {
    setFormData((prev) => {
      return prev.map((f: any) =>
        f.title === field ? { ...f, value } : f
      );
    });
  };

  const handleSubmit = () => {
    const result = validationSchema.safeParse(formData);
    if (!result.success) {
      const errorMessages = result.error.format();
      setErrors(errorMessages);
    } else {
      setErrors({});
      // Submit the form data (you can handle API submission here)
      console.log("Form Submitted:", formData);
    }
  };

  const openEditModal = (field: any) => {
    setActiveField(field);
    setIsEditing(true);
  };

  const closeEditModal = () => {
    setIsEditing(false);
    setActiveField(null);
  };

  const renderField = (field: any) => {
    const { type, title, description, enabled, value, fields } = field;

    if (!enabled) return null;

    // Recursively handle children (nested fields)
    if (type === "children" && fields) {
      return (
        <div key={title} className="mb-4" style={{color:"black"}}>
          <div className="flex justify-between items-center">
            <h3 className="text-xl font-semibold">{title}</h3>
            <button
              onClick={() => openEditModal(field)}
              className="bg-blue-600 text-white py-1 px-3 rounded hover:bg-blue-700"
            >
              Edit
            </button>
          </div>
          <p className="text-gray-500">{description}</p>
          <div className="ml-6">
            {fields.map((childField: any) => renderField(childField))}
          </div>
        </div>
      );
    }

    // Render simple fields like text, email, phone, etc.
    return (
      <div key={title} className={`mb-4 ${value?.length > 50 ? 'grid grid-cols-2 gap-4' : ''}`}>
        <div className="flex justify-between items-center">
          <label className="block text-sm font-semibold">{title}</label>
          <button
            onClick={() => openEditModal(field)}
            className="bg-blue-600 text-white py-1 px-3 rounded hover:bg-blue-700"
          >
            Edit
          </button>
        </div>
        <p className="text-gray-500">{description}</p>
        <p className="text-lg">{value}</p>
        {errors[title] && <p className="text-red-500 text-sm">{errors[title]?.message}</p>}
      </div>
    );
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <h1 className="text-2xl font-bold mb-6">Edit Your Profile</h1>

      <form onSubmit={(e) => e.preventDefault()}>
        {formData.map((field: any) => renderField(field))}

        <div className="flex justify-between items-center mt-6">
          <button
            onClick={handleSubmit}
            className="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700"
          >
            Save Changes
          </button>
        </div>
      </form>

      {isEditing && (
        <div className="fixed inset-0 flex justify-center items-center bg-gray-500 bg-opacity-50">
          <div className="bg-white p-6 rounded-lg shadow-lg w-96">
            <h2 className="text-xl font-semibold mb-4">{activeField?.title}</h2>
            <input
              type={activeField?.type}
              value={activeField?.value || ""}
              onChange={(e) => handleChange(activeField?.title, e.target.value)}
              className="w-full px-3 py-2 border rounded-md mt-2"
            />
            <div className="flex justify-end mt-4">
              <button
                onClick={closeEditModal}
                className="bg-gray-400 text-white py-1 px-3 rounded mr-2"
              >
                Cancel
              </button>
              <button
                onClick={() => { handleChange(activeField?.title, activeField?.value); closeEditModal(); }}
                className="bg-blue-600 text-white py-1 px-3 rounded"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ProfileForm;
