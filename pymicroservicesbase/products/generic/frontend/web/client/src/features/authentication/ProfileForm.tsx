"use client";

import { useActionState, useEffect, useState } from "react";
import NProgress from 'nprogress';
import {updateUserProfile} from "../../app/dashboard/profile/actions"

function getDescriptionForField(field) {
  const descriptions = {
    firstName: "Your given name, as it appears on your account.",
    lastName: "Your family name or surname.",
    email: "The email address associated with your account.",
    username: "Your unique username for login and display purposes.",
    phoneNumber: "The phone number linked to your account for contact.",
    dateOfBirth: "Your birth date for account personalization.",
    address: "Your current residential address.",
  };

  return descriptions[field] || "Additional information for your profile.";
}

const initialState = {
  message:"",
  errors:null
}


export default function ProfileForm({ userData }) {
  const [state, formAction, pending] = useActionState(updateUserProfile, initialState);
  const [formData, setFormData] = useState<any>(userData);
  const [editingField, setEditingField] = useState(null);
  const [editValue, setEditValue] = useState("");
  const [error, setError] = useState("");

  const handleSave = () => {
    if (!formData.email.includes("@")) {
      setError("Invalid email address. Please provide a valid email.");
      return;
    }
    if (!formData.username) {
      setError("Username cannot be empty.");
      return;
    }
    setError("");
    alert(`Profile updated:\n${JSON.stringify(formData, null, 2)}`);
  };

  const openModal = (field, currentValue) => {
    setEditingField(field);
    setEditValue(currentValue);
  };

  const saveEdit = () => {
    if (!editValue.trim()) {
      setError(`${editingField} cannot be empty.`);
      return;
    }
    setFormData((prev) => ({ ...prev, [editingField]: editValue }));
    setEditingField(null);
    setError("");
  };

  const closeModal = () => setEditingField(null);
  useEffect(() => {
    if (pending) {
      NProgress.start();
    } else {
      NProgress.done();
    }

    return () => {
      NProgress.done();
    };
  }, [pending]);

  return (
    <div className="bg-gray-50 p-10 rounded-lg shadow-lg">
      <h1 className="text-4xl font-bold text-gray-800 mb-8 text-center">
        Profile Settings
      </h1>

      {state?.errors && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
          <span>{"errors"}</span>
        </div>
      )}

      <form action={formAction}>
        {Object.entries(formData).map(([field, value]) => (
          <div key={field} className="mb-6 bg-gray-100 border border-gray-400 text-red-700 px-4 py-3 rounded mb-6">
            <label className="block text-lg font-semibold text-gray-700 capitalize mb-1">
              {field.replace(/([A-Z])/g, " $1").toLowerCase()}
            </label>
            <p className="text-sm text-gray-500 mb-2">
              {getDescriptionForField(field)}

            </p>
            {/* <input
              id={field.name}
              name={"identifier"}
            /> */}
            <div className="flex items-center justify-between">

              <span className="text-gray-800 text-base p-3">{value || "Not set"}</span>

              <button
                type="button"
                disabled={pending}
                onClick={() => openModal(field, value)}
                className="text-black hover:text-black-700 text-sm font-semibold"
              >
                Edit
              </button>
            </div>
          </div>
        ))}
        <div className="mt-10 text-center">
          <button
            disabled={pending}
            type="submit"
            className="bg-blue-600 text-white px-6 py-3 rounded shadow-lg hover:bg-blue-700 focus:outline-none focus:ring-4 focus:ring-blue-300"
          >
            Save Changes
          </button>
        </div>
      </form>

      {/* Modal for editing */}
      {editingField && (
        <div className="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
          <div className="bg-white p-6 rounded-lg shadow-lg max-w-sm w-full">
            <h2 className="text-2xl font-bold text-gray-800 mb-6">
              Edit {editingField.replace(/([A-Z])/g, " $1").toLowerCase()}
            </h2>
            <input
              type="text"
              disabled={pending}
              style={{color:"black"}}
              value={editValue}
              onChange={(e) => setEditValue(e.target.value)}
              className="w-full p-3 border border-gray-300 rounded-lg mb-6"
              placeholder={`Enter new ${editingField}`}
            />
            <div className="flex justify-end">
              <button
                disabled={pending}
                type="button"
                onClick={closeModal}
                className="text-gray-500 hover:text-gray-700 mr-4"
              >
                Cancel
              </button>
              <button
                disabled={pending}
                type="button"
                onClick={saveEdit}
                className="bg-blue-600 text-white px-4 py-2 rounded shadow-lg hover:bg-blue-700"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
