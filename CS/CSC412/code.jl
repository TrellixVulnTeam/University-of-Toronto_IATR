losses = [[10, 0],
          [1, 50],
          [0, 200]]


num_actions = length(losses)


function expected_loss_of_action(prob_spam, action)
    #TODO: Return expected loss over a Bernoulli random variable
    #      with mean prob_spam.
    #      Losses are given by the table above.
    losses = [[10, 0],
              [1, 50],
              [0, 200]]
    loss = losses[action]
    length_prob_spam = length(prob_spam)



    non_prob = 1 .- prob_spam
    expect_loss = [prob_spam[i]*loss[1]+non_prob[i]*loss[2] for i in 1:length_prob_spam]
    return expect_loss
end

prob_range = range(0., stop=1., length=500)

using Plots
for action in 1:num_actions
  display(plot!(prob_range, expected_loss_of_action(prob_range, action)))
end

function optimal_action(prob_spam)
    #TODO: return best action given the probability of spam.
    # Hint: Julia's findmin function might be helpful.

    losses = [[10, 0],[1, 50],[0, 200]]
    non_prob_spam = 1-prob_spam
    expected_loss = []
    for i in 1:3
        loss = losses[i]
        push!(expected_loss, loss[1]*prob_spam+loss[2]*non_prob_spam)
    end
    return findmin(expected_loss)
end

prob_range = range(0, stop=1., length=500)
optimal_losses = []
optimal_actions = []
for p in prob_range
    # TODO:  Compute the optimal action and its expected loss for
    # probability of spam given by p.
    res = optimal_action(p)
    push!(optimal_losses,res[1])
    push!(optimal_actions,res[2])

end
optimal_actions
plot(prob_range, optimal_losses, linecolor=optimal_actions)
