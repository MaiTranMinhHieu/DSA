def loop_invariant_proof():
    proof_lines = [
        "Sau luot thu i, i phan tu lon nhat da nam dung vi tri o cuoi mang.",
        "Do do, sau n luot, toan bo mang se duoc sap xep va thuat toan ket thuc hop le."
    ]
    return "\n".join(proof_lines)

if __name__ == "__main__":
    proof_result = loop_invariant_proof()
    print(proof_result)