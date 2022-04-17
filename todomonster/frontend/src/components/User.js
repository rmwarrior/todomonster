import React from "react";


const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                {user.id}
            </td>
            <td>
                {user.first_name}
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
            </td>
        </tr>
    )
}


const UserList = ({users}) => {
    return(
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Birthday year</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user}/>)}
            </tbody>
        </table>
    )
}


export default UserList
