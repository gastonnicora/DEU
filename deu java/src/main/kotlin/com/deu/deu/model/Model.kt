package com.deu.deu.model

import com.fasterxml.jackson.annotation.JsonIgnore
import jakarta.persistence.*
import java.util.Date

@Entity
@Table(name = "appUser")
data class User(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    val name: String,
    val email: String,
    val password: String,
    @Enumerated(EnumType.STRING)
    val type: UserType,
    @Enumerated(EnumType.STRING)
    val position: Position? = null,
    @ManyToMany(mappedBy = "users")
    val teams: List<Team> = listOf()
)

@Entity
data class Exercise(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    val name: String,
    val description: String,
    val time: Int?,
    @Enumerated(EnumType.STRING)
    val units: UnitsType?,
    val count: Int,
    val type: TimeType,
    val category: ExerciseType,
    @ManyToOne
    val video: Video,
    val isVisible: Boolean
)

@Entity
data class Video(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    val name: String,
    val url: String
)

@Entity
data class Training(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    val name: String,
    val description: String?,
    @ManyToOne
    val trainer: User,
    val date: Date,
    @Enumerated(EnumType.STRING)
    val type: TrainingType,
    @OneToMany(cascade = [CascadeType.ALL])
    val comments: List<Comment>?
)

@Entity
data class Comment(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    @ManyToOne
    val idUser: User,
    val comment: String
)

@Entity
data class Config(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    @OneToOne
    val idUser: User,
    @Enumerated(EnumType.STRING)
    val theme: ThemeType
)

@Entity
data class Team(
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    val id: Int = 0,
    val name: String,
    @ManyToMany
    @JsonIgnore
    @JoinTable(
        name = "user_team",
        joinColumns = [JoinColumn(name = "team_id")],
        inverseJoinColumns = [JoinColumn(name = "user_id")]
    )
    val users: List<User> = listOf()
)
