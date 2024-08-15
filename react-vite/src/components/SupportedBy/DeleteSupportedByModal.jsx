import { useModal } from "../../context/Modal";

function DeleteReviewModal({ onDelete }) {
  const { closeModal } = useModal();

  const handleDelete = async () => {
    await onDelete();
    closeModal();
  };

  return (
    <div id="container-delete-review-modal">
      <h1>Confirm Deletion</h1>
      <p>Are you sure you want to delete?</p>
      <div className="modal-buttons">
        <button onClick={handleDelete}>Yes, Delete</button>
        <button onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteReviewModal;
